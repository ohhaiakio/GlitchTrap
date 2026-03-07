from libnmap.parser import NmapParser

def diff_me_baby(new_path, old_path):

    new = NmapParser.parse_fromfile(new_path)
    old = NmapParser.parse_fromfile(old_path)

    new_items_changed = new.diff(old).changed()
    changed_host_id = new_items_changed.pop().split('::')[1]

    changed_host_new = new.get_host_byid(changed_host_id)
    changed_host_old = old.get_host_byid(changed_host_id)
    host_new_items_changed = changed_host_new.diff(changed_host_old).changed()

    changed_service_id = host_new_items_changed.pop().split('::')[1]
    changed_service_new = changed_host_new.get_service_byid(changed_service_id)
    changed_service_old = changed_host_old.get_service_byid(changed_service_id)
    service_new_items_changed = changed_service_new.diff(changed_service_old).changed()

def main():
    diff_me_baby('/home/akio/git/OldManTouchy/results/old.xml', '/home/akio/git/OldManTouchy/results/new.xml')