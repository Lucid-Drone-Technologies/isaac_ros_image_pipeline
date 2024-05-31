# SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES
# Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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

from typing import Any, Dict

from isaac_ros_examples import IsaacROSLaunchFragment
from launch_ros.descriptions import ComposableNode


class IsaacROSColorConversionLaunchFragment(IsaacROSLaunchFragment):

    @staticmethod
    def get_composable_nodes(interface_specs: Dict[str, Any]) -> Dict[str, ComposableNode]:
        return {
            'color_conversion_node': ComposableNode(
                package='isaac_ros_image_proc',
                plugin='nvidia::isaac_ros::image_proc::ImageFormatConverterNode',
                name='color_conversion',
                namespace='',
                parameters=[{
                    'encoding_desired': 'mono8',
                    'image_width': interface_specs['camera_resolution']['width'],
                    'image_height': interface_specs['camera_resolution']['height'],
                }],
                remappings=[
                    ('image', 'image_mono'),
                ]
            ),
        }
