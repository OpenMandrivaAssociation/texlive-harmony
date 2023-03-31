Name:		texlive-harmony
Version:	15878
Release:	2
Summary:	Typeset harmony symbols, etc., for musicology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/harmony
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harmony.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harmony.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package harmony.sty uses the packages ifthen and amssymb
from the amsfonts bundle, together with the LaTeX font
lcirclew10 and the font musix13 from musixtex.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/harmony/harmony.sty
%doc %{_texmfdistdir}/doc/latex/harmony/README
%doc %{_texmfdistdir}/doc/latex/harmony/harmony.pdf
%doc %{_texmfdistdir}/doc/latex/harmony/harmony.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
