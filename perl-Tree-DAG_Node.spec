%include	/usr/lib/rpm/macros.perl
Summary:	Tree-DAG_Node perl module
Summary(pl):	Modu³ perla Tree-DAG_Node
Name:		perl-Tree-DAG_Node
Version:	1.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tree/Tree-DAG_Node-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tree/DAG_Node
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Tree/DAG_Node.pm
%{perl_sitearch}/auto/Tree/DAG_Node

%{_mandir}/man3/*
