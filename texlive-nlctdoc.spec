Name:		texlive-nlctdoc
Epoch:		1
Version:	74438
Release:	1
Summary:	Package documentation class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nlctdoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nlctdoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nlctdoc.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/nlctdoc
%doc %{_texmfdistdir}/doc/latex/nlctdoc

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
