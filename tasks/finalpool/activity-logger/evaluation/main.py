from evaluation.main import run_evaluation
from utils.evaluation.evaluator import run_task

if __name__ == '__main__':
    run_task(
        agent_short_name='activity-logger',
        task_dir='tasks/lueyang/activity-logger',
    )
