%define	pdir	Tree
%define	pnam	DAG_Node
%include	/usr/lib/rpm/macros.perl
Summary:	Tree-DAG_Node perl module
Summary(pl):	Modu³ perla Tree-DAG_Node
Name:		perl-Tree-DAG_Node
Version:	1.04
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tree-DAG_Node perl module.

%description -l pl
Modu³ perla Tree-DAG_Node.

%prep
%setup -q -n Tree-DAG_Node-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tree/DAG_Node.pm
%{_mandir}/man3/*
