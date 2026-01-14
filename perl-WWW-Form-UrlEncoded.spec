#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	WWW
%define		pnam	Form-UrlEncoded
Summary:	WWW::Form::UrlEncoded - parser and builder for application/x-www-form-urlencoded
Name:		perl-WWW-Form-UrlEncoded
Version:	0.26
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cbe0e1c3ee54738d900c739ea348efda
URL:		http://search.cpan.org/dist/WWW-Form-UrlEncoded/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-JSON >= 2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Form::UrlEncoded provides application/x-www-form-urlencoded
parser and builder. This module aims to have compatibility with other
CPAN modules like HTTP::Body's urlencoded parser.

This module try to use WWW::Form::UrlEncoded::XS by default and fail
to it, use WWW::Form::UrlEncoded::PP instead

WWW::Form::UrlEncoded parsed string in this rule.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--destdir=$RPM_BUILD_ROOT \
	--installdirs=vendor
BREAK_BACKWARD_COMPAT=1 ./Build

%{?with_tests:BREAK_BACKWARD_COMPAT=1 ./Build test}

%install
rm -rf $RPM_BUILD_ROOT

BREAK_BACKWARD_COMPAT=1 ./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/WWW/Form
%{perl_vendorlib}/WWW/Form/*.pm
%{perl_vendorlib}/WWW/Form/UrlEncoded
%{_mandir}/man3/WWW::Form::UrlEncoded*.3*
%{_examplesdir}/%{name}-%{version}
