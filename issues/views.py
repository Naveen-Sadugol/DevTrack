import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Reporter, Issue, CriticalIssue, LowPriorityIssue


# ---------------- Utility ----------------
def read_json(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except:
        return []


def write_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)


# ---------------- Reporter APIs ----------------
@csrf_exempt
def reporters(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            reporter = Reporter(
                data['id'],
                data['name'],
                data['email'],
                data['team']
            )
            reporter.validate()

            reporters_list = read_json('reporters.json')
            reporters_list.append(reporter.to_dict())
            write_json('reporters.json', reporters_list)

            return JsonResponse(reporter.to_dict(), status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == "GET":
        reporters_list = read_json('reporters.json')

        reporter_id = request.GET.get('id')

        if reporter_id:
            for r in reporters_list:
                if r['id'] == int(reporter_id):
                    return JsonResponse(r, status=200)
            return JsonResponse({"error": "Reporter not found"}, status=404)

        return JsonResponse(reporters_list, safe=False)


# ---------------- Issue APIs ----------------
@csrf_exempt
def issues(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Choose subclass
            if data['priority'] == 'critical':
                issue = CriticalIssue(**data)
            elif data['priority'] == 'low':
                issue = LowPriorityIssue(**data)
            else:
                issue = Issue(**data)

            issue.validate()

            issues_list = read_json('issues.json')

            issue_data = issue.to_dict()
            issue_data['created_at'] = str(datetime.now())
            issue_data['message'] = issue.describe()

            issues_list.append(issue_data)
            write_json('issues.json', issues_list)

            return JsonResponse(issue_data, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == "GET":
        issues_list = read_json('issues.json')

        issue_id = request.GET.get('id')
        status_filter = request.GET.get('status')

        if issue_id:
            for issue in issues_list:
                if issue['id'] == int(issue_id):
                    return JsonResponse(issue, status=200)
            return JsonResponse({"error": "Issue not found"}, status=404)

        if status_filter:
            filtered = [i for i in issues_list if i['status'] == status_filter]
            return JsonResponse(filtered, safe=False)

        return JsonResponse(issues_list, safe=False)
