# revision 32705
# category Package
# catalog-ctan /macros/latex/contrib/nlctdoc
# catalog-date 2014-01-17 19:05:21 +0100
# catalog-license lppl
# catalog-version 1.04
Name:		texlive-nlctdoc
Epoch:		1
Version:	1.06
Release:	2
Summary:	Package documentation class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nlctdoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nlctdoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nlctdoc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides support for the documentation of the
author's packages, using koma-script. This class is provided
"as is" solely for the benefit of anyone who wants to compile
the documentation of those packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nlctdoc/nlctdoc.cls
%doc %{_texmfdistdir}/doc/latex/nlctdoc/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
