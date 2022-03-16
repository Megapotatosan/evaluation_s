
# TrackEval
*Code for evaluating object tracking.*

## Evaluate on your own custom benchmark

To evaluate on your own data, you have two options:
 - Write custom dataset code (more effort, rarely worth it).
 - Convert your current dataset and trackers to the same format of an already implemented benchmark.


By default, recommend the MOTChallenge format, although any implemented format should work. Note that for many cases you will want to use the argument ```--DO_PREPROC False``` unless you want to run preprocessing to remove distractor objects.

## Requirements

use ```pip3 -r install requirements.txt``` to install all possible requirements.

use ```pip3 -r install minimum_requirments.txt``` to only install the minimum if you don't need the extra functionality as listed above.

## Usage
use ```python run.py`` under the demo directory
