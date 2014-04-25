%define upstream_name    Net-OpenID-Consumer
%define upstream_version 1.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Object representing a verified OpenID identity

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::DH)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl(URI)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(CGI)
BuildArch:	noarch

%description
This module provides an implementation of the Yadis protocol, which does
XRDS-based service discovery on URLs.

This module was originally developed by OHTSUKA Ko-hei as the
Net::Yadis::Discovery manpage, but was forked and simplified for inclusion
in the core OpenID Consumer package.

This simplified version is tailored for the needs of Net::OpenID::Consumer;
for other uses, the Net::Yadis::Discovery manpage is probably a better
choice.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


