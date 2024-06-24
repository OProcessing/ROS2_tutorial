# generated from
# rosidl_cmake/cmake/template/rosidl_cmake_export_typesupport_targets.cmake.in

set(_exported_typesupport_targets
  "__rosidl_generator_c:my_first_package_msgs__rosidl_generator_c;__rosidl_typesupport_fastrtps_c:my_first_package_msgs__rosidl_typesupport_fastrtps_c;__rosidl_typesupport_introspection_c:my_first_package_msgs__rosidl_typesupport_introspection_c;__rosidl_typesupport_c:my_first_package_msgs__rosidl_typesupport_c;__rosidl_generator_cpp:my_first_package_msgs__rosidl_generator_cpp;__rosidl_typesupport_fastrtps_cpp:my_first_package_msgs__rosidl_typesupport_fastrtps_cpp;__rosidl_typesupport_introspection_cpp:my_first_package_msgs__rosidl_typesupport_introspection_cpp;__rosidl_typesupport_cpp:my_first_package_msgs__rosidl_typesupport_cpp;__rosidl_generator_py:my_first_package_msgs__rosidl_generator_py")

# populate my_first_package_msgs_TARGETS_<suffix>
if(NOT _exported_typesupport_targets STREQUAL "")
  # loop over typesupport targets
  foreach(_tuple ${_exported_typesupport_targets})
    string(REPLACE ":" ";" _tuple "${_tuple}")
    list(GET _tuple 0 _suffix)
    list(GET _tuple 1 _target)

    set(_target "my_first_package_msgs::${_target}")
    if(NOT TARGET "${_target}")
      # the exported target must exist
      message(WARNING "Package 'my_first_package_msgs' exports the typesupport target '${_target}' which doesn't exist")
    else()
      list(APPEND my_first_package_msgs_TARGETS${_suffix} "${_target}")
    endif()
  endforeach()
endif()
