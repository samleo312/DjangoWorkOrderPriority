from .mongodb_client import mongodb_client

class Resource:
    CATEGORY_CHOICES = [('controls', 'Controls'),
                        ('mes', 'MES'),
                        ('maintenance', 'Maintenance'),
                        ('other', 'Other')]

    def __init__(self, name, capacity, category):
        self.name = name
        self.capacity = capacity
        self.category = category

    def save(self):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_resource']
        collection.insert_one({
            'name': self.name,
            'capacity': self.capacity,
            'category': self.category
        })

    def __str__(self):
        return self.name

class AddedWorkOrder:
    AREA_CHOICES = [('jyd', 'JYD'),
                    ('sprayDry', 'Spray Dry'),
                    ('tableting', 'Tableting'),
                    ('nonProduction', 'Non-Production')]

    CATEGORY_CHOICES = [('controls', 'Controls'),
                        ('mes', 'MES'),
                        ('maintenance', 'Maintenance'),
                        ('other', 'Other')]

    def __init__(self, priority, woNumber, description, requestedBy, resourcePriority, notes, area, category, status):
        self.priority = priority
        self.woNumber = woNumber
        self.description = description
        self.requestedBy = requestedBy
        self.resourcePriority = resourcePriority
        self.notes = notes
        self.area = area
        self.category = category
        self.status = status

    def save(self):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_addedworkorder']
        collection.insert_one({
            'priority': self.priority,
            'woNumber': self.woNumber,
            'description': self.description,
            'requestedBy': self.requestedBy,
            'resourcePriority': self.resourcePriority,
            'notes': self.notes,
            'area': self.area,
            'category': self.category,
            'status': self.status
        })

    def __str__(self):
        return self.woNumber

class UnaddedWorkOrder:
    def __init__(self, instructions, status_date, closed_date, dispatch, total_cost, requested_due_date, externalid, parent_workorder, scheduled_date, parent_dispatch, number, createdby, lastupdatedby, id, labor_cost, created, spares_estimate, priority, createdbyuser, kit_template, estimated_cost, estimated_hours, spares_cost, status, parent_fives, description, owner_assigned_date, requestedby_phone, requestedby, project_workorder, actual_hours, parent_kaizen, parent_sigevent, costcenter, projectid, owner, lastupdatedbyuser, product, due_date, site, trade, machine, closed, lastupdated, launch_date, category, external_cost, attachment_count, area):
        self.instructions = instructions
        self.status_date = status_date
        self.closed_date = closed_date
        self.dispatch = dispatch
        self.total_cost = total_cost
        self.requested_due_date = requested_due_date
        self.externalid = externalid
        self.parent_workorder = parent_workorder
        self.scheduled_date = scheduled_date
        self.parent_dispatch = parent_dispatch
        self.number = number
        self.createdby = createdby
        self.lastupdatedby = lastupdatedby
        self.id = id
        self.labor_cost = labor_cost
        self.created = created
        self.spares_estimate = spares_estimate
        self.priority = priority
        self.createdbyuser = createdbyuser
        self.kit_template = kit_template
        self.estimated_cost = estimated_cost
        self.estimated_hours = estimated_hours
        self.spares_cost = spares_cost
        self.status = status
        self.parent_fives = parent_fives
        self.description = description
        self.owner_assigned_date = owner_assigned_date
        self.requestedby_phone = requestedby_phone
        self.requestedby = requestedby
        self.project_workorder = project_workorder
        self.actual_hours = actual_hours
        self.parent_kaizen = parent_kaizen
        self.parent_sigevent = parent_sigevent
        self.costcenter = costcenter
        self.projectid = projectid
        self.owner = owner
        self.lastupdatedbyuser = lastupdatedbyuser
        self.product = product
        self.due_date = due_date
        self.site = site
        self.trade = trade
        self.machine = machine
        self.closed = closed
        self.lastupdated = lastupdated
        self.launch_date = launch_date
        self.category = category
        self.external_cost = external_cost
        self.attachment_count = attachment_count
        self.area = area

    def save(self):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_unaddedworkorder']
        collection.insert_one({
            'instructions': self.instructions,
            'status_date': self.status_date,
            'closed_date': self.closed_date,
            'dispatch': self.dispatch,
            'total_cost': self.total_cost,
            'requested_due_date': self.requested_due_date,
            'externalid': self.externalid,
            'parent_workorder': self.parent_workorder,
            'scheduled_date': self.scheduled_date,
            'parent_dispatch': self.parent_dispatch,
            'number': self.number,
            'createdby': self.createdby,
            'lastupdatedby': self.lastupdatedby,
            'id': self.id,
            'labor_cost': self.labor_cost,
            'created': self.created,
            'spares_estimate': self.spares_estimate,
            'priority': self.priority,
            'createdbyuser': self.createdbyuser,
            'kit_template': self.kit_template,
            'estimated_cost': self.estimated_cost,
            'estimated_hours': self.estimated_hours,
            'spares_cost': self.spares_cost,
            'status': self.status,
            'parent_fives': self.parent_fives,
            'description': self.description,
            'owner_assigned_date': self.owner_assigned_date,
            'requestedby_phone': self.requestedby_phone,
            'requestedby': self.requestedby,
            'project_workorder': self.project_workorder,
            'actual_hours': self.actual_hours,
            'parent_kaizen': self.parent_kaizen,
            'parent_sigevent': self.parent_sigevent,
            'costcenter': self.costcenter,
            'projectid': self.projectid,
            'owner': self.owner,
            'lastupdatedbyuser': self.lastupdatedbyuser,
            'product': self.product,
            'due_date': self.due_date,
            'site': self.site,
            'trade': self.trade,
            'machine': self.machine,
            'closed': self.closed,
            'lastupdated': self.lastupdated,
            'launch_date': self.launch_date,
            'category': self.category,
            'external_cost': self.external_cost,
            'attachment_count': self.attachment_count,
            'area': self.area
        })

    def __str__(self):
        return self.number
