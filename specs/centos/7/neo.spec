Name: intel-opencl
Version: 19.45.14764
Release: 1%{?dist}
Summary: Intel(R) Graphics Compute Runtime for OpenCL(TM)

Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/compute-runtime
Source0: %{url}/archive/%{version}/compute-runtime-%{version}.tar.gz

BuildRequires: centos-release-scl epel-release
BuildRequires: devtoolset-7-gcc-c++ cmake3 make
BuildRequires: intel-gmmlib-devel = 19.3.4
BuildRequires: intel-igc-opencl-devel = 1.0.2805

Requires: intel-gmmlib = 19.3.4
Requires: intel-igc-opencl = 1.0.2805

%description
Intel(R) Graphics Compute Runtime for OpenCL(TM).

%prep
%autosetup -n compute-runtime-%{version}

%build
mkdir build
cd build
scl enable devtoolset-7 'cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/usr -DNEO_DRIVER_VERSION=%{version} -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" -DSKIP_UNIT_TESTS=1 ..'
scl enable devtoolset-7 "make -j`nproc`"

%install
cd build
%make_install
chmod +x ${RPM_BUILD_ROOT}/usr/lib64/intel-opencl/libigdrcl.so

%files
/usr/lib64/intel-opencl/libigdrcl.so
/usr/bin/ocloc

%config(noreplace)
/etc/OpenCL/vendors/intel.icd

%doc

%changelog
* Tue Nov 19 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.45.14764-1
- Update to 19.45.14764

* Wed Nov 13 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.44.14658-1
- Update to 19.44.14658

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.43.14583-1
- Update to 19.43.14583

* Thu Oct 24 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.41.14441-1
- Update to 19.41.14441

