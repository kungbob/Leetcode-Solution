class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = []
        domains = dict()
        for domain in cpdomains:
            completeUrl = ""
            chop = domain.split(' ')
            count = int(chop[0])
            url = chop[1]
            subdomains = url.split('.')
            for subdomain in reversed(subdomains):
                completeUrl = subdomain + completeUrl
                if completeUrl in domains:
                    domains[completeUrl] += count
                else:
                    domains[completeUrl] = count
                completeUrl = '.' + completeUrl
        for key in domains:
            result.append(str(domains[key]) + ' ' + key)
        return result