. ~/ros2_humble/install/local_setup.bash
ros2 run demo_nodes_py listener
locale
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
locale
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo jammy) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update && sudo apt install -y
sudo apt update && sudo apt install -y   python3-flake8-docstrings   python3-pip   python3-pytest-cov   ros-dev-tools
sudo apt install -y    python3-flake8-blind-except    python3-flake8-builtins    python3-flake8-class-newline    python3-flake8-comprehensions    python3-flake8-deprecated    python3-flake8-import-order    python3-flake8-quotes    python3-pytest-repeat    python3-pytest-rerunfailures
mkdir -p ~/ros2_humble/src
cd ~/ros2_humble
vcs import --input https://raw.githubusercontent.com/ros2/ros2/humble/ros2.repos src
sudo apt upgrade
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers" --os=ubuntu:jammy --rosdistro=humble
colcon build --symlink-install
colcon build --symlink-install --event-handlers console_direct+ --log-level debug
colcon build --symlink-install --event-handlers console_direct+
colcon logs
ros2 run rviz2 rviz2
cd
. ~/ros2_humble/install/local_setup.bash
ros2 run demo_nodes_cpp talker
. ~/ros2_humble/install/local_setup.bash
QT_QPA_PLATFORM=xcb rviz2
rviz2
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talke
ros2 run demo_nodes_cpp talker
ource ~/ros2_humble/install/local_setup.bash
source ~/ros2_humble/install/local_setup.bash
ls
echo $ROS_DISTRO
source ros2_humble/install/
. ~/ros2_humble/install/local_setup.bash
echo $ROS_DISTRO
ls
sudo nano .bashrc 
sudo reboot
sudo apt update
sudo apt upgrade
ip addr show
ls
ros2 -h
exi
ls
exit
ls
pwd
eixt
exit
ros2 topic list
cd bumperbot_ws/
rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
rm -rf build install log
colcon build --symlink-install
cd
sudo nano .bashrc 
pip install transform3d
sudo apt install ros-humble-geographic-msgs -y
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y
sudo apt --fix-broken install
sudo apt install ros-humble-geographic-msgs -y
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup -y
ls
cd ros2_humble
ls
cd
mkdir -p ~/nav2_ws/src
ls
cd nav2_ws/
git clone https://github.com/ros-planning/navigation2.git
git clone https://github.com/ros-planning/navigation_msgs.git
rosdep update
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
git clone https://github.com/ros-geographic-info/geographic_info.git
rosdep update
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
cd ~/nav2_ws/src
rm -rf geographic_info
ls
git clone https://github.com/ros2/common_interfaces.git -b humble src/geographic_msgs
rosdep update
cd ..
rosdep update
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install --allow-overriding map_msgs
cd
rm -r nav2_ws
sudo rm -rf nav2_ws
ls
cd ros2_humble
reboot
sudo reboot
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world
dokcer version
docker version
clear
sudo usermod -aG docker $USER
sudo docker run  arm64v8/ros:humble
docker run -it --name ros2_humble_container     --privileged --network=host     -v /home/pi/humble_docker:/workspace     -w /workspace     -v /dev:/dev     arm64v8/ros:humble
groups pi
sudo usermod -aG docker pi
docker run -it --name ros2_humble_container     --privileged --network=host     -v /home/pi/humble_docker:/workspace     -w /workspace     -v /dev:/dev     arm64v8/ros:humble
sudo systemctl status docker
sudo systemctl restart docker
docker run -it --name ros2_humble_container     --privileged --network=host     -v /home/pi/humble_docker:/workspace     -w /workspace     -v /dev:/dev     arm64v8/ros:humble
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
df
clear
cd humble_docker/
pwd
docker exec -it ros2_humble_container bash
docker start ros2_humble_container
docker exec -it ros2_humble_container bash
docker start ros2_humble_container
docker exec -it ros2_humble_container bash
sudo reboot
docker exec -it ros2_humble_container bash
docker stop ros2_humble_docker 
docker 
docker stop ros2_humble_container
docker exec -it ros2_humble_container bash
ls
python3 face_recog_camera.py 
sudo nano face_recog_camera.py 
python3 face_recog_camera.py 
pip install imutils
sudo apt install python3-imutils
sudo apt install pipx
pipx install imutils
python3 -c "import imutils; print(imutils.__version__)"
pipx ensurepath
python3 -c "import imutils; print(imutils.__version__)"
ls
sudo nanno face_recog_camera.py 
sudo nano face_recog_camera.py 
python face_recog_camera.py Duy
python3 face_recog_camera.py Duy
pip install imutils
pip install imutils --break-system-packages
python3 face_recog_camera.py Duy
pip install opencv-python
pip install opencv-python --break-system-packages
python3 face_recog_camera.py Duy
pip install face_recognition --break-system-packages
python3 face_recog_camera.py Duy
pip install gpiod
pip install gpiod --break-system-packages
python3 face_recog_camera.py Duy
ls
sudo nano face_recog_camera.py 
python3 face_recog_camera.py Duy
ls /dev/gpiochip*
gpiodetect
gpioinfo gpiochip0
sudo apt update
sudo apt install gpiod -y
gpioinfo gpiochip0
gpioget gpiochip0 17
gpioset gpiochip0 17=1
gpioget gpiochip0 17
gpioget gpiochip0 17=1
gpioset gpiochip0 17=1
gpioget gpiochip0 17
ls
python3 test_gpio.py 
gpioget gpiochip0 17
ls -l /dev/gpiochip0
sudo usermod -aG gpio pi
sudo reboot
ls
groups pi
ls -l /dev/gpiochip0
sudo python3 test_gpio.py
sudo nano test_gpio.py 
sudo python3 test_gpio.py
sudo apt install python3-libgpiod -y
sudo python3 test_gpio.py
sudo python3 test_gpio.py
ls -l /dev/gpiochip0
gpioset gpiochip0 17=1
gpioset gpiochip0 17=0
gpioset gpiochip0 17=1
gpioset gpiochip0 17=0
gpioset gpiochip0 17=1
gpioset gpiochip0 17=0
sudo nano face_recog_camera.py Duy
python3 face_recog_camera.py Duy
sudo nano face_recog_camera.py
python3 face_recog_camera.py Duy
python3 test_gpio.py 
python3 face_recog_camera.py Duy
gpioset gpiochip0 17=1
python3 face_recog_camera.py Duy
gpioset gpiochip0 17=0
python3 face_recog_camera.py Duy
gpioset gpiochip0 17=0
python3 face_recog_camera.py Duy
gpioset gpiochip0 17=0
python3 face_recog_camera.py Duy
python3 face_recog_camera.py
gpioset gpiochip0 17=0
python3 face_recog_camera.py
sudo shutdown now
python3 face_recog_camera.py
gpioset gpiochip0 17=1
gpioset gpiochip0 17=0
python3 face_recog_camera.py
sudo apt-get install -y gpiod
gpioinfo
sudo gpioinfo
python3 face_recog_camera.py
sudo python3 face_recog_camera.py
python3 face_recog_camera.py
python3 face_recog_camera.py Duy
python3 face_recog_camera.py Lan
python3 face_recog_camera.py
python3 face_recog_camera.py 
python3 face_recog_camera.py Lan
gpioset gpiochip0 17=0
sudo shutdown now
humble
start
humble
start
humble
docker stop ros2_humble_container
docker ps
start
docker ps
start
docker start ros2_humble_container
docker stop ros2_humble_container
docker ps
start
docker start ros2_humble_container
sudo nano .bashrc 
start
sudo reboot
sudo nano /etc/netplan/50-cloud-init.yaml 
sudo netplan apply
sudo nano /etc/netplan/50-cloud-init.yaml 
sudo reboot
humble
sudo nano /etc/netplan/50-cloud-init.yaml 
docker ps
start
docker ps
start docker
start
humble 
sudo shutdown now
ls
humble
humble 
humble
start
humble
ros2 topic list
cd bumperbot_ws/
. install/setup.bash 
sudo reboot
humnle
humble 
exit
start
humble 
humble 
humble
sudo reboot
start
humble 
sudo reboot
humble 
humble
humble 
sudo shutdown now
humble
exit
ip addr show
ip addr show 
docker network create --driver bridge --subnet=172.16.36.0/22 humble_docker
docker network ls
docker network rm humble_docker 
docker network ls
start
humble 
humble
sudo reboot now
start
humble 
docker stop ros2_humble_container
docker network ls 
ip addr show
start
humble
docker stop ros2_humble_container
docker inspect humble_docker | grep "IPAddress"
docker inspect ros2_humnle_container | grep "IPAddress"
docker inspect ros2_humble_container | grep "IPAddress"
docker inspect ros2_humble_container | grep "NetworkMode"
docker ps
star
start
docker ps
exit
ros2 run nav2_map_server map_saver_cli -f map
humble 
humble
humble
start
docker ps
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ros2_humble_container
humble
start
humbl
humble
sudo reboot
humnle
humble 
humble
start
humble 
humble
start
humble
sudo reboot
start
humble
sudo reboot 
humble
ls
sudo shutdown now
ls
exit
start
humnle
humble 
humble
sudo reboot 
start
humble 
sudo shutdown now
humble
humbl
humble
sudo shutdown no
sudo shutdown now
start
humble
sudo shutdown now
