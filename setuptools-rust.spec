#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools-rust
Version  : 0.12.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/12/22/6ba3031e7cbd6eb002e13ffc7397e136df95813b6a2bd71ece52a8f89613/setuptools-rust-0.12.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/12/22/6ba3031e7cbd6eb002e13ffc7397e136df95813b6a2bd71ece52a8f89613/setuptools-rust-0.12.1.tar.gz
Summary  : Setuptools Rust extension plugin
Group    : Development/Tools
License  : MIT
Requires: setuptools-rust-license = %{version}-%{release}
Requires: setuptools-rust-python = %{version}-%{release}
Requires: setuptools-rust-python3 = %{version}-%{release}
Requires: beautifulsoup4
Requires: cffi
Requires: lxml
Requires: setuptools
Requires: toml
Requires: wheel
BuildRequires : beautifulsoup4
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : lxml
BuildRequires : pip
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : toml
BuildRequires : wheel

%description
# Setuptools plugin for Rust extensions
![example workflow](https://github.com/PyO3/setuptools-rust/actions/workflows/ci.yml/badge.svg)
[![pypi package](https://badge.fury.io/py/setuptools-rust.svg)](https://badge.fury.io/py/setuptools-rust)
[![readthedocs](https://readthedocs.org/projects/pip/badge/)](https://setuptools-rust.readthedocs.io/en/latest/)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package license
Summary: license components for the setuptools-rust package.
Group: Default

%description license
license components for the setuptools-rust package.


%package python
Summary: python components for the setuptools-rust package.
Group: Default
Requires: setuptools-rust-python3 = %{version}-%{release}

%description python
python components for the setuptools-rust package.


%package python3
Summary: python3 components for the setuptools-rust package.
Group: Default
Requires: python3-core
Provides: pypi(setuptools_rust)
Requires: pypi(semantic_version)
Requires: pypi(setuptools)
Requires: pypi(toml)

%description python3
python3 components for the setuptools-rust package.


%prep
%setup -q -n setuptools-rust-0.12.1
cd %{_builddir}/setuptools-rust-0.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622655010
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/setuptools-rust
cp %{_builddir}/setuptools-rust-0.12.1/LICENSE %{buildroot}/usr/share/package-licenses/setuptools-rust/b6d59af9754634678ceb503c91126c4248bf14c3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/setuptools-rust/b6d59af9754634678ceb503c91126c4248bf14c3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
