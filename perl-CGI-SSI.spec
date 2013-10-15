%define upstream_name    CGI-SSI
%define upstream_version 0.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Use SSI from CGI scripts
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Date::Format)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(HTML::SimpleParse)
BuildRequires: perl(HTTP::Cookies)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(URI)
BuildRequires: perl-devel
BuildArch: noarch

%description
CGI::SSI is meant to be used as an easy way to filter shtml through CGI
scripts in a loose imitation of Apache's mod_include. If you're using
Apache, you may want to use either mod_include or the Apache::SSI module
instead of CGI::SSI. Limitations in a CGI script's knowledge of how the
server behaves make some SSI directives impossible to imitate from a CGI
script.

Most of the time, you'll simply want to filter shtml through STDOUT or some
other open filehandle. 'autotie' is available for STDOUT, but in general,
you'll want to tie other filehandles yourself:

    $ssi = tie(*FH, 'CGI::SSI', filehandle => 'FH');
    print FH $shtml;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*
