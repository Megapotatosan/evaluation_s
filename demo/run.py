import sys
import os
import argparse
from multiprocessing import freeze_support

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import trackeval  # noqa: E402

if __name__ == '__main__':
	freeze_support()

	# Command line interface:
	default_eval_config = trackeval.Evaluator.get_default_eval_config()
	default_eval_config['DISPLAY_LESS_PROGRESS'] = False
	default_dataset_config = trackeval.datasets.MotChallenge2DBox.get_default_dataset_config()
	default_metrics_config = {'METRICS': ['HOTA'], 'THRESHOLD': 0.5}
	config = {**default_eval_config, **default_dataset_config, **default_metrics_config}  # Merge default configs

	eval_config = {k: v for k, v in config.items() if k in default_eval_config.keys()}
	dataset_config = {k: v for k, v in config.items() if k in default_dataset_config.keys()}
	metrics_config = {k: v for k, v in config.items() if k in default_metrics_config.keys()}

	root_folder = '/home/sgi/evaluation'
	output_folder = '/home/sgi/evaluation/result'
	eval_config['LOG_ON_ERROR'] = output_folder

	dataset_config['GT_FOLDER'] = '%s' % root_folder
	dataset_config['TRACKERS_FOLDER'] = '%s/predictions' % root_folder
	dataset_config['OUTPUT_FOLDER'] = output_folder
	dataset_config['TRACKERS_TO_EVAL'] = ['yolov5s', 'yolov5m', 'yolov5l', 'yolov5x'] # Filenames of trackers to eval (if None, all in folder)
	dataset_config['BENCHMARK'] = 'missy_office'
	dataset_config['SPLIT_TO_EVAL'] = 'test'
	dataset_config['SEQMAP_FILE'] = '%s/%s-%s/seqmaps.txt' % (dataset_config['GT_FOLDER'], dataset_config['BENCHMARK'], dataset_config['SPLIT_TO_EVAL'])


	# Run code
	evaluator = trackeval.Evaluator(eval_config)
	dataset_list = [trackeval.datasets.MotChallenge2DBox(dataset_config)]
	metrics_list = []
	for metric in [trackeval.metrics.HOTA, trackeval.metrics.CLEAR, trackeval.metrics.Identity, trackeval.metrics.VACE]:
		if metric.get_name() in metrics_config['METRICS']:
			metrics_list.append(metric(metrics_config))
	if len(metrics_list) == 0:
		raise Exception('No metrics selected for evaluation')
	evaluator.evaluate(dataset_list, metrics_list)
