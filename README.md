# Robotic-Arm-with-ROS
### This project was done for simulating a 3 DOF robotic arm.

**Running the simulation on Rviz:**
```
roslaunch manipulator_description manipulator.launch
```
![Screenshot from 2022-12-04 11-36-58](https://user-images.githubusercontent.com/65026915/205477126-0ee63735-2f69-45c1-82c6-9d2e141baf17.png)

**Spawning the urdf file in Gazebo:**
```
roslaunch manipulator_description spawn.launch
```

Also open the Gazebo window using 
```
rosrun gazebo_ros gazebo
```

![Screenshot from 2022-12-04 11-43-10](https://user-images.githubusercontent.com/65026915/205477266-d7974ae3-08d3-49df-a3db-6e4b26cdf37f.png)

This urdf model also has a depth camera fixed to the base_link in front of the robotic arm
You can visualize the camera image using rqt_image_view or using rviz also

**For visualizing camera image using rqt_image_view:**
```
rosrun rqt_image_view rqt_image_view
```
and then select the `/camera/color/image_raw` topic to visualize the colored image

![Screenshot from 2022-12-04 11-43-23](https://user-images.githubusercontent.com/65026915/205477339-288e8b41-90e6-4177-ac82-8d39dc2675a2.png)

Here, the image shows the box placed infront of the camera

For visualizing depth image using rqt_image_view:
select the `/camera/depth/image_raw` topic to visualize the depth image

![Screenshot from 2022-12-04 11-49-53](https://user-images.githubusercontent.com/65026915/205477414-4df46310-0e48-4874-92d3-bdfc1d72374f.png)

Here, the image shows the depth image indicating the distances of the objects infront of camera


The pkg_moveit_manipulator package includes the moveit configuration of the urdf file

**For the demo of robotic arm simulation:**
```
roslaunch pkg_moveit_manipulator demo.launch
```

It opens up a Rviz window where you can use MotionPlanning tab to plan the motion of the Arm and the Gripper as well..

Choose a Goal State and click on Plan & Execute button to execute the path planning for Arm

[Screencast from 04-12-22 11:58:36 AM IST.webm](https://user-images.githubusercontent.com/65026915/205477933-85813293-7c0e-4b14-8053-b1c7f9b81f07.webm)

Similarly for the Gripper Group 
First change the `Planning group` from Arm to Gripper and then Choose a Goal State and click on Plan & Execute button to execute the path planning for Gripper

[Screencast from 04-12-22 12:00:28 PM IST.webm](https://user-images.githubusercontent.com/65026915/205477970-dbcd9c3e-6226-4451-8a0e-dd0d72282f91.webm)


