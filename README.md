An exploration of fault-tolerant networks using the RYU SDN framework
=====================================================================

### Repository Contents
The repository contains code for experiments that measure the properties of fault-correction in software defined networks.
The `mininet` tool is used to emulate a physical network of routers and hosts, and the `ryu` OpenFlow controller is used to determine the global network topology, detect link failures, and perform appropriate re-routing actions.

### Running the Code
To run the code, do the following:
* Ensure that the `openvswitch` daemon is active. On Arch Linux I do this by running `sudo systemctl start openvswitch`.
* Create and activate a Python 3.9 virtual environment. On Arch Linux, I use pyenv to manage multiple versions of python.
* Install the dependencies with `pip install -r requirements.txt`.
* Run the RYU app with `ryu-manager ryu-fault-detector.py`.
* Start the mininet with `sudo python mn.py`.

### Experiments
TODO
Two network performance parameters are measured in our experiments: Latency and Recovery time. We expect our controller to route packets along the shortest available path from source to destination. When a link is brought down, the controller is responsible for re-routing packets along the next-best path.

We measure these parameters for three different network topologies.

### Credits
Code and documentation written by Carsten Thue-Bludworth, Misael Deniz, and Bogachan Ondes for University of Florida class EEL5718 - "Computer Communications" taught by Janise McNair, Summer 2022.