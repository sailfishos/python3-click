# fixme: should be defined in base system side
%define python3_sitelib %(%{__python3} -Ic "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name: python3-click
Summary: python package for creating beautiful command line interfaces
Version: 7.1.2
Release: 1
License: BSD-3-Clause
Group: Development/Languages
URL: https://github.com/pallets/click
Source0: %{name}-%{version}.tar.bz2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Click is a Python package for creating beautiful command line
interfaces in a composable way with as little code as necessary.

%prep
%setup -q -n %{name}-%{version}/python-click

%build
CFLAGS="%{optflags}" %{__python3} setup.py build %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/click
%{python3_sitelib}/click-*.egg-info/



