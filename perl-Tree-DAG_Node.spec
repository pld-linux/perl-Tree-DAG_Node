%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	DAG_Node
Summary:	Tree::DAG_Node - (super)class for representing nodes in a tree
Name:		perl-Tree-DAG_Node
Version:	1.04
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class encapsulates/makes/manipulates objects that represent nodes
in a tree structure. The tree structure is not an object itself, but is
emergent from the linkages you create between nodes.  This class provides
the methods for making linkages that can be used to build up a tree,
while preventing you from ever making any kinds of linkages which are not
allowed in a tree (such as having a node be its own mother or ancestor,
or having a node have two mothers).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
