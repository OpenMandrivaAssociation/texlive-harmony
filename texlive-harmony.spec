# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/harmony
# catalog-date 2009-06-25 00:34:53 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-harmony
Version:	20090625
Release:	1
Summary:	Typeset harmony symbols, etc., for musicology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/harmony
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harmony.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harmony.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package harmony.sty uses the packages ifthen and amssymb
from the amsfonts bundle, together with the LaTeX font
lcirclew10 and the font musix13 from musixtex.

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
%{_texmfdistdir}/tex/latex/harmony/harmony.sty
%doc %{_texmfdistdir}/doc/latex/harmony/README
%doc %{_texmfdistdir}/doc/latex/harmony/harmony.pdf
%doc %{_texmfdistdir}/doc/latex/harmony/harmony.tex
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
