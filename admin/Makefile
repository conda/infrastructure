allrepos:
	@gh api orgs/conda/repos --paginate | jq ".[] | .name"

allteams:
	@gh api orgs/conda/teams --paginate | jq ".[] | .name"

allmembers:
	@gh api orgs/conda/members --paginate | jq ".[] | .login,.type"

teaminfos:
	@gh api orgs/conda/teams --paginate | jq ".[] | .name"| xargs -I {} gh api "orgs/conda/teams/{}/members" --paginate


.PHONY: $(MAKECMDGOALS)


# cp admin/team-members.csv.tpl "admin/team-members/{}.csv"


# make allteams | xargs -i {} cp admin/team-members.csv.tpl "admin/team-members/{}.csv"
