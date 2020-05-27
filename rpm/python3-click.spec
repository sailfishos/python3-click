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
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/click
%{python3_sitelib}/click-*.egg-info/



