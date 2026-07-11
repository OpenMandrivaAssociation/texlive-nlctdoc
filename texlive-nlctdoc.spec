%global tl_name nlctdoc
%global tl_revision 79421

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.18
Release:	%{tl_revision}.1
Summary:	Package documentation class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nlctdoc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nlctdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nlctdoc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class provides support for the documentation of the author's
packages, using koma-script. This class is provided "as is" solely for
the benefit of anyone who wants to compile the documentation of those
packages.

