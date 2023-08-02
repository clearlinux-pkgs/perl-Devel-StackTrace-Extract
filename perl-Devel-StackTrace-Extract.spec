#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Devel-StackTrace-Extract
Version  : 1.000000
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Devel-StackTrace-Extract-1.000000.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Devel-StackTrace-Extract-1.000000.tar.gz
Summary  : 'Extract a stack trace from an exception object'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Devel-StackTrace-Extract-license = %{version}-%{release}
Requires: perl-Devel-StackTrace-Extract-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Devel::StackTrace::Frame)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
Devel::StackTrace::Extract - Extract a stack trace from an exception object

%package dev
Summary: dev components for the perl-Devel-StackTrace-Extract package.
Group: Development
Provides: perl-Devel-StackTrace-Extract-devel = %{version}-%{release}
Requires: perl-Devel-StackTrace-Extract = %{version}-%{release}

%description dev
dev components for the perl-Devel-StackTrace-Extract package.


%package license
Summary: license components for the perl-Devel-StackTrace-Extract package.
Group: Default

%description license
license components for the perl-Devel-StackTrace-Extract package.


%package perl
Summary: perl components for the perl-Devel-StackTrace-Extract package.
Group: Default
Requires: perl-Devel-StackTrace-Extract = %{version}-%{release}

%description perl
perl components for the perl-Devel-StackTrace-Extract package.


%prep
%setup -q -n Devel-StackTrace-Extract-1.000000
cd %{_builddir}/Devel-StackTrace-Extract-1.000000

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-StackTrace-Extract
cp %{_builddir}/Devel-StackTrace-Extract-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Devel-StackTrace-Extract/6dc8469576e79fb276656dcca354a3d87bd53057 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::StackTrace::Extract.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-StackTrace-Extract/6dc8469576e79fb276656dcca354a3d87bd53057

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
