#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB17327D40171DF30 (jannis@leidel.info)
#
Name     : django-discover-runner
Version  : 1.0
Release  : 43
URL      : https://files.pythonhosted.org/packages/d3/60/5ffffcfb2306afd1f67cb7fb820eba66033a2cb4aceda131d8f9c47ff2af/django-discover-runner-1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d3/60/5ffffcfb2306afd1f67cb7fb820eba66033a2cb4aceda131d8f9c47ff2af/django-discover-runner-1.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/d3/60/5ffffcfb2306afd1f67cb7fb820eba66033a2cb4aceda131d8f9c47ff2af/django-discover-runner-1.0.tar.gz.asc
Summary  : A Django test runner based on unittest2's test discovery.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-discover-runner-license = %{version}-%{release}
Requires: django-discover-runner-python = %{version}-%{release}
Requires: django-discover-runner-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
======================

%package license
Summary: license components for the django-discover-runner package.
Group: Default

%description license
license components for the django-discover-runner package.


%package python
Summary: python components for the django-discover-runner package.
Group: Default
Requires: django-discover-runner-python3 = %{version}-%{release}

%description python
python components for the django-discover-runner package.


%package python3
Summary: python3 components for the django-discover-runner package.
Group: Default
Requires: python3-core
Provides: pypi(django_discover_runner)

%description python3
python3 components for the django-discover-runner package.


%prep
%setup -q -n django-discover-runner-1.0
cd %{_builddir}/django-discover-runner-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603391018
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/django-discover-runner
cp %{_builddir}/django-discover-runner-1.0/LICENSE %{buildroot}/usr/share/package-licenses/django-discover-runner/556234559d76a6b42aa5d22d9baad7cbd44fece9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/django-discover-runner/556234559d76a6b42aa5d22d9baad7cbd44fece9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
