# SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES
# Copyright (c) 2021-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    resize_node = ComposableNode(
        package='isaac_ros_image_proc',
        plugin='nvidia::isaac_ros::image_proc::ResizeNode',
        name='resize',
        parameters=[{
            'output_width': 480,
            'output_height': 288,
        }],
        remappings=[
            ('image', 'hawk_0_left_rgb_image'),
            ('camera_info', 'hawk_0_left_rgb_camera_info'),
        ])

    resize_container = ComposableNodeContainer(
        package='rclcpp_components',
        name='resize_container',
        namespace='',
        executable='component_container_mt',
        composable_node_descriptions=[
            resize_node,
        ],
        output='screen'
    )

    return launch.LaunchDescription([resize_container])
