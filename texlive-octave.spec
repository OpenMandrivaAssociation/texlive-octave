Name:		texlive-octave
Version:	45674
Release:	1
Summary:	Typeset musical pitches with octave designations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/octave
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/octave.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/octave.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package package typesets musical pitch names with
designation for the octave in either the Helmholtz system (with
octave numbers), or the traditional system (with prime
symbols). Authors can just write \pitch{C}{4} and the pitches
will be rendered correctly depending on which package option
was selected. The system can also be changed mid-document.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/octave
%doc %{_texmfdistdir}/doc/latex/octave

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
