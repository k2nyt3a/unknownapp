import json
import os

def view_course_catalog():
    # Path to the json file based on your project structure
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'courses.json')
    
    try:
        with open(file_path, 'r') as f:
            courses = json.load(f)
            
        print("=" * 70)
        print("   COURSE CATALOG (Python Version)")
        print("=" * 70)
        print(f"{'Code':<10} {'Title':<25} {'Credits':<10} {'Seats':<10}")
        print("-" * 70)
        
        for course in courses:
            # Matching the output style seen in your Java terminal
            code = course.get('code', 'N/A')
            title = course.get('title', 'N/A')
            credits = course.get('credits', 0)
            capacity = course.get('capacity', 0)
            enrolled = len(course.get('enrolledStudentIds', []))
            
            print(f"{code:<10} {title:<25} {credits:<10} {enrolled}/{capacity}")
            
        print("=" * 70)
        
    except FileNotFoundError:
        print(f"[Error] Could not find courses.json at {file_path}")

if __name__ == "__main__":
    view_course_catalog()