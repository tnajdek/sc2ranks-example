#!/usr/bin/env python2

from sc2ranks.core import Sc2Ranks

api_key = 'doppnet.com'
client = Sc2Ranks('api_key')

print "Search Character"
name = raw_input('Enter name: ').strip()
# print name
response = client.search_for_character(region="eu", name=name)

characters = list()
options = list()
total = response.total
if(response.total > 10):
	total = 10

for i in range(total):
	options.append(['eu', response.characters[i]['name'], response.characters[i]['bnet_id']])
characters = client.fetch_mass_characters_team(options, bracket="1v1")
	

counter = 0
lookup = dict()
for c in characters:
	counter = counter+1

	teams = list()
	for team in c.teams:
		team = "%i in %s (%i)" % (team.division_rank, team.league, team.points)
		teams.append(team)
	print "%i - %s [points %i]; %s" % (counter, c.name, c.achievement_points, ','.join(teams)) 
	lookup[counter] = c

selected = int(raw_input("Enter number to select character (1..%i): " % counter).strip())
character = lookup[selected]

print "\n"
print "------ Profile summary for %s ------" % character.name
print "Total of %i achievement points" % character.achievement_points
print "\n"
for type in ["1v1", "2v2", "3v3", "4v4"]:
	res = client.fetch_character_teams("eu", character.name, character.bnet_id, type)
	if(res.teams):
		print "In %s matchup" % type
		for team in res.teams:
			print "\t%i in %s (%i)" % (team.division_rank, team.league, team.points)
	else: 
		print "Not ranked in %s matchup" % type

print "###################################"
print "\n"
# import ipdb;
# ipdb.set_trace();	