check_mk_sensu
==============

A Sensu plugin that will parse data from the check_mk windows agent and output "metric" data formatted for the Graphite handler

In my efforts to move away from nagios/Icinga to Sensu I created this script to make use of the great check_mk windows (and maybe unix) agent as there does not appear to be many checks for windows and Sensu. And this allows me to keep using already deployed agents for windows machines.  Currently this script will parse the disk and memory information and will export out in Graphite friendly format 
