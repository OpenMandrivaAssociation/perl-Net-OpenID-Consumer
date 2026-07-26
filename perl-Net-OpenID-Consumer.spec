%define upstream_name    Net-OpenID-Consumer
Name:		perl-%{upstream_name}
Version:	1.18
Release:	2

Summary:	Object representing a verified OpenID identity
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/wrog/Net-OpenID-Consumer
Source0:	https://cpan.metacpan.org/authors/id/W/WR/WROG/Net-OpenID-Consumer-%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 655425
- add br
- rebuild for updated spec-helper

* Mon Apr 26 2010 Nicolas Vigier <nvigier@mandriva.com> 1.30.0-1mdv2011.0
+ Revision: 539225
- import perl-Net-OpenID-Consumer


* Mon Apr 26 2010 cpan2dist 1.03-1mdv
- initial mdv release, generated with cpan2dist

