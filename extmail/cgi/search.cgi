#!/usr/bin/perl -wT
# vim: set cindent expandtab ts=4 sw=4:
use vars qw($DIR);

BEGIN {
    if ($ENV{SCRIPT_FILENAME} =~ m!(.*/)cgi!) {
        $DIR = $1;
    }else {
        $DIR = '../';
    }
    my $path = $DIR . 'libs';
    unshift @INC, $path unless grep /^$path$/, @INC;

    #print "content-type: text/html\r\n\r\n";
    #$SIG{__WARN__} = $SIG{__DIE__} = sub { print @_ };
}
use strict;

eval {
    require Ext::App::Search;
    my $app = Ext::App::Search->new( config => $DIR.'webmail.cf',
                                    directory => $DIR );
    $app->run;
};

if ($@) {
    print "Content-type: text/html\r\n\r\n";
    print "$@";
}
