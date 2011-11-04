# revision 18976
# category Package
# catalog-ctan /macros/latex/contrib/nlctdoc
# catalog-date 2010-06-14 15:23:50 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-nlctdoc
Version:	20100614
Release:	1
Summary:	Package documentation class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nlctdoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nlctdoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nlctdoc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The class provides support for the documentation of the
author's packages. This class is provided "as is" solely for
the benefit of anyone who wants to compile the documentation of
those packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nlctdoc/nlctdoc.cls
%doc %{_texmfdistdir}/doc/latex/nlctdoc/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}