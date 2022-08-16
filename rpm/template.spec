%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-rosbridge-test-msgs
Version:        1.3.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rosbridge_test_msgs package

License:        BSD
URL:            http://ros.org/wiki/rosbridge_library
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-builtin-interfaces
Requires:       ros-galactic-geometry-msgs
Requires:       ros-galactic-rclpy
Requires:       ros-galactic-rosidl-default-runtime
Requires:       ros-galactic-std-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-builtin-interfaces
BuildRequires:  ros-galactic-geometry-msgs
BuildRequires:  ros-galactic-rosidl-default-generators
BuildRequires:  ros-galactic-std-msgs
BuildRequires:  ros-galactic-ros-workspace
BuildRequires:  ros-galactic-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-galactic-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-galactic-rosidl-interface-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-galactic-actionlib-msgs
BuildRequires:  ros-galactic-ament-cmake-pytest
BuildRequires:  ros-galactic-diagnostic-msgs
BuildRequires:  ros-galactic-example-interfaces
BuildRequires:  ros-galactic-nav-msgs
BuildRequires:  ros-galactic-sensor-msgs
BuildRequires:  ros-galactic-std-srvs
BuildRequires:  ros-galactic-stereo-msgs
BuildRequires:  ros-galactic-tf2-msgs
BuildRequires:  ros-galactic-trajectory-msgs
BuildRequires:  ros-galactic-visualization-msgs
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-galactic-rosidl-interface-packages(all)
%endif

%description
Message and service definitions used in internal tests for rosbridge packages.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Tue Aug 16 2022 Jihoon Lee <jihoonlee.in@gmail.com> - 1.3.0-1
- Autogenerated by Bloom

* Fri May 20 2022 Jihoon Lee <jihoonlee.in@gmail.com> - 1.2.0-1
- Autogenerated by Bloom

* Mon Jan 03 2022 Jihoon Lee <jihoonlee.in@gmail.com> - 1.1.2-1
- Autogenerated by Bloom

* Thu Dec 09 2021 Jihoon Lee <jihoonlee.in@gmail.com> - 1.1.1-1
- Autogenerated by Bloom

* Fri Oct 22 2021 Jihoon Lee <jihoonlee.in@gmail.com> - 1.1.0-1
- Autogenerated by Bloom

