repo system 0 testtags <inline>
#>=Pkg: A 1 1 i686
#>=Pkg: B 1 1 noarch
#>=Pkg: C 1 2 i686
#>=Pkg: D 1 1 i686
#>=Pkg: D 1 1 x86_64
#>=Pkg: E 1 1 x86_64
repo available 0 testtags <inline>
#>=Pkg: A 2 1 noarch
#>=Pkg: A 3 1 x86_64
#>=Pkg: B 2 1 x86_64
#>=Pkg: C 1 3 x86_64
#>=Pkg: D 2 1 x86_64
system x86_64 rpm system

poolflags implicitobsoleteusescolors
solverflags keeporphans allowuninstall
job distupgrade all packages
result transaction,problems <inline>
#>upgrade A-1-1.i686@system A-2-1.noarch@available
#>upgrade B-1-1.noarch@system B-2-1.x86_64@available

nextjob
poolflags implicitobsoleteusescolors
solverflags keeporphans
job distupgrade all packages
result transaction,problems <inline>
#>upgrade A-1-1.i686@system A-2-1.noarch@available
#>upgrade B-1-1.noarch@system B-2-1.x86_64@available
