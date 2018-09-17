
class Filter:

    def filter_store(self, element):

        list_to_filter = []
        for item in element:
            item = item.strip()
            item = item.lower()
            list_to_filter.append(item)
        return list(set(list_to_filter))