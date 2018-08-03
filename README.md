Data Science Toolbox (DST)

Project Structure
------------
~~~
.
├── README.md
├── data
├── common
│   ├── analysis
│   ├── config
│   ├── dataset
│   ├── exceptions
│   ├── logger
│   ├── plot
│   └── utils
└── scripts
    └── test_analysis
        ├── config.cfg
        └── run.py

~~~

In addition to the above, temporary folders such as output, logs would be created (they are not checked-in).

Pre-requisites
------------
1. Python 3.0
2. numpy: http://docs.scipy.org/doc/numpy-1.10.1/user/install.html
3. matplotlib: http://matplotlib.org/faq/installing_faq.html#install-osx-binaries
4. scipy: http://www.scipy.org/install.html (optional)

**Note**: Verified to run only on Mac OSX so far.

Usage
------------
i) Test Analysis

cd scripts/test_analysis
Run "python run.py" (by default it will run all the analysis)
use -h to print help
use -r to run
use -c to specify a config file (by default it uses the one in configs folder)


### Contact ###
[1] Santhoshkumar Sunderrajan( santhoshkumar.sunderrajan@gmail.com)

**Website:** http://santhoshsunderrajan.com/

[2] Aravind Sunderrajan (aravind.sunderrajan@gmail.com)


### Disclaimer ###
We may have used some good codes from various sources, please feel free to notify me if you find a piece of code that I need to acknowledge.

