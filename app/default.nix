# default.nix
with (import <nixpkgs> {});
let
  python-packages = python-packages: with python-packages; [
    jinja2
  ];
  python-with-packages = python39.withPackages python-packages;
in
mkShell {
  buildInputs = [
    python-with-packages
    python39Packages.pip
  ];
}
