#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-discover-runner
Version  : 1.0
Release  : 17
URL      : https://pypi.python.org/packages/source/d/django-discover-runner/django-discover-runner-1.0.tar.gz
Source0  : https://pypi.python.org/packages/source/d/django-discover-runner/django-discover-runner-1.0.tar.gz
Summary  : A Django test runner based on unittest2's test discovery.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-discover-runner-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
django-discover-runner
======================
.. note::
This runner has been added to Django 1.6 as the default test runner.
If you use Django 1.6 or above you don't need this app.

%package python
Summary: python components for the django-discover-runner package.
Group: Default

%description python
python components for the django-discover-runner package.


%prep
%setup -q -n django-discover-runner-1.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
