# Comparison-of-Anomaly-Detection-Approaches
Experiments conducted for CS 6480 class project.

Prog.py is run to log system calls.

Cuckoo.py performs following actions:

  * Reads training data from a file and populates Cuckoo filter.
  * Reads live data from a file and performs set membership operations on Cuckoo filter to detect anomalies.
