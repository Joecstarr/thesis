{
  description = "Flake for mystmd";

  inputs = { nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable"; };

  outputs = { self, nixpkgs, }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      #   tex = pkgs.texlive.combine {
      #     inherit (pkgs.texlive)
      #       scheme-tetex
      #       collection-luatex
      #       adjustbox
      #       amsmath
      #       bbm
      #       background
      #       biblatex
      #       capt-of
      #       catchfile
      #       datetime
      #       doi
      #       enumitem
      #       environ
      #       everypage
      #       fancyhdr
      #       fmtcount
      #       fncychap
      #       fontaxes
      #       fontspec
      #       framed
      #       glossaries
      #       graphbox
      #       graphics
      #       hyperref
      #       ifoddpage
      #       import
      #       latexmk
      #       lipsum
      #       listings
      #       mdframed
      #       needspace
      #       pdfcol
      #       relsize
      #       sauerj
      #       silence
      #       svg
      #       tabulary
      #       tcolorbox
      #       tikzfill
      #       titlesec
      #       transparent
      #       upquote
      #       varwidth
      #       wrapfig
      #       xcharter
      #       xetex
      #       xstring
      #       xurl
      #       zref
      #       commonunicode
      #       newunicodechar
      #       gnu-freefont
      #       ;
      #   };
    in {

      devShells.${system}.default = pkgs.mkShell {

        buildInputs = with pkgs; [
          act
          imagemagick
          python3
          inkscape
          just
          nodejs
          nodePackages.prettier
          nodePackages_latest.svgo
          rip2
          rsync
          tectonic
          ruff
          svg2pdf
          uv
          wget
          zip
        ];
        LOCALE_ARCHIVE = "${pkgs.glibcLocales}/lib/locale/locale-archive";
        NIX_LD_LIBRARY_PATH =
          pkgs.lib.makeLibraryPath [ pkgs.stdenv.cc.cc pkgs.libz ];

        shellHook = ''
          export DBUS_SESSION_BUS_ADDRESS=""
          wget -q --spider https://google.com

          if [ $? -eq 0 ]; then
              echo "Online"
              rip .venv
              just bootstrap
          else
              echo "Offline"
          fi
          source .venv/bin/activate
          echo done!
        '';
      };
    };
}
