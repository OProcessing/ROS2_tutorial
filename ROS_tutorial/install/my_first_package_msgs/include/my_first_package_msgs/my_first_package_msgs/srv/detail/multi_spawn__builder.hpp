// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_first_package_msgs:srv/MultiSpawn.idl
// generated code does not contain a copyright notice

#ifndef MY_FIRST_PACKAGE_MSGS__SRV__DETAIL__MULTI_SPAWN__BUILDER_HPP_
#define MY_FIRST_PACKAGE_MSGS__SRV__DETAIL__MULTI_SPAWN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_first_package_msgs/srv/detail/multi_spawn__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_first_package_msgs
{

namespace srv
{

namespace builder
{

class Init_MultiSpawn_Request_num
{
public:
  Init_MultiSpawn_Request_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_first_package_msgs::srv::MultiSpawn_Request num(::my_first_package_msgs::srv::MultiSpawn_Request::_num_type arg)
  {
    msg_.num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_first_package_msgs::srv::MultiSpawn_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_first_package_msgs::srv::MultiSpawn_Request>()
{
  return my_first_package_msgs::srv::builder::Init_MultiSpawn_Request_num();
}

}  // namespace my_first_package_msgs


namespace my_first_package_msgs
{

namespace srv
{

namespace builder
{

class Init_MultiSpawn_Response_theta
{
public:
  explicit Init_MultiSpawn_Response_theta(::my_first_package_msgs::srv::MultiSpawn_Response & msg)
  : msg_(msg)
  {}
  ::my_first_package_msgs::srv::MultiSpawn_Response theta(::my_first_package_msgs::srv::MultiSpawn_Response::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_first_package_msgs::srv::MultiSpawn_Response msg_;
};

class Init_MultiSpawn_Response_y
{
public:
  explicit Init_MultiSpawn_Response_y(::my_first_package_msgs::srv::MultiSpawn_Response & msg)
  : msg_(msg)
  {}
  Init_MultiSpawn_Response_theta y(::my_first_package_msgs::srv::MultiSpawn_Response::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_MultiSpawn_Response_theta(msg_);
  }

private:
  ::my_first_package_msgs::srv::MultiSpawn_Response msg_;
};

class Init_MultiSpawn_Response_x
{
public:
  Init_MultiSpawn_Response_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MultiSpawn_Response_y x(::my_first_package_msgs::srv::MultiSpawn_Response::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_MultiSpawn_Response_y(msg_);
  }

private:
  ::my_first_package_msgs::srv::MultiSpawn_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_first_package_msgs::srv::MultiSpawn_Response>()
{
  return my_first_package_msgs::srv::builder::Init_MultiSpawn_Response_x();
}

}  // namespace my_first_package_msgs

#endif  // MY_FIRST_PACKAGE_MSGS__SRV__DETAIL__MULTI_SPAWN__BUILDER_HPP_
