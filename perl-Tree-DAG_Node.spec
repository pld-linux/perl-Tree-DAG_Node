%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	DAG_Node
Summary:	Tree::DAG_Node - (super)class for representing nodes in a tree
Summary(pl):	Tree::DAG_Node - (nad)klasa do reprezentowania wêz³ów w drzewie
Name:		perl-Tree-DAG_Node
Version:	1.04
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class encapsulates/makes/manipulates objects that represent nodes
in a tree structure. The tree structure is not an object itself, but
is emergent from the linkages you create between nodes. This class
provides the methods for making linkages that can be used to build up
a tree, while preventing you from ever making any kinds of linkages
which are not allowed in a tree (such as having a node be its own
mother or ancestor, or having a node have two mothers).

%description -l pl
Ta klasa obudowuje, tworzy i obrabia obiekty, które reprezentuj± wêz³y
w strukturze drzewiastej. Struktura drzewiasta jako taka nie jest
obiektem, ale wy³ania siê z po³±czeñ tworzonych pomiêdzy wêz³ami. Ta
klasa udostêpnia metody do tworzenia po³±czeñ, które mog± byæ u¿ywane
do zbudowania drzewa, nie dopuszczaj±c na zrobienie po³±czeñ nie
dozwolonych w drzewie (takich jak po³±czenie wêz³a z jego przodkiem,
lub nadanie wêz³owi dwóch przodków).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Tree/DAG_Node.pm
%{_mandir}/man3/*
