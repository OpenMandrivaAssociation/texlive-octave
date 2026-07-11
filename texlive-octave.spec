%global tl_name octave
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset musical pitches with octave designations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/octave
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/octave.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/octave.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package typesets musical pitch names with designation for the
octave in either the Helmholtz system (with octave numbers), or the
traditional system (with prime symbols). Authors can just write
\pitch{C}{4} and the pitches will be rendered correctly depending on
which package option was selected. The system can also be changed mid-
document.

