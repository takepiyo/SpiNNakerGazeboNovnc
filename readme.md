# SpiNNaker and Gazebo environment

This repository is designed to be built with vscode devcontainer.

after open container, do `source ~/.bashrc`
## check python development env(Intellisense debugging etc..)
maybe useful `check_env/python_check.py`

## install spinnaker and check simulation
```
pip install matplotlib
pip install sPyNNaker
python -m spynnaker8.setup_pynn
python -c "import pyNN.spiNNaker as sim; sim.setup(); sim.end()"
cp /workspaces/SpiNNakerGazeboVNC/assets/.spynnaker.cfg ~/.spynnaker.cfg
python check_env/spinnaker_check.py
```
check output figure.png

if you want to check connect spinnaker board in the ISI lab, do `ping 192.168.240.1`

### Check operation with a simple example
another terminal open and
```
cd ~/catkin_ws/src
cd ~/catkin_ws && catkin_make
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
cd ~/catkin_ws && catkin_make
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
cd ~/catkin_ws/src
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws && catkin_make
```
launch turtlebot
`roslaunch turtlebot3_gazebo turtlebot3_world.launch`
`roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

launch gzclient via noVNC
local terminal
`ssh remote_server -N -f -L 6080:localhost:6080`
open `http://localhost:6080` in browser
open terminal in brouwser desktop and command
`gzclient`
It will show turtlebot gazebo env. Also can teleop...

## install ros spinnaker interface
```
git clone https://github.com/takepiyo/ros_spinnaker_interface.git
pip install -e ros_spinnaker_interface
```

## install rviz web
https://github.com/osrf/rvizweb

<!-- ## install ros -->

<!-- ## intsall gzweb(view gaezbo simlation via browser)
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
source ~/.bashrc
nvm install 8
cd ~; git clone https://github.com/osrf/gzweb
cd ~/gzweb
git checkout gzweb_1.4.1
source /usr/share/gazebo/setup.sh
npm run deploy --- -m
```
https://osrf-migration.github.io/gzweb-gh-pages/#!/osrf/gzweb/issues/61/page/1
cp -r /usr/share/gazebo-11/media/ ~/gzweb/http/client/assets/
### start gzweb server background
```
cd ~/gzweb && npm start
```
### connect gzweb
port forwarding 8080 on the local terminal
`ssh remote_server -N -f -L 8080:localhost:8080`
open browser at `http://localhost:8080` -->