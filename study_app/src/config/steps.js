/**
 * Static master configuration for every participant's flow.
 * Step IDs that contain `task:` are dynamically expanded into a concrete
 * task/modality step using the participant's assignment.
 *
 * NOTE: the consent form, baseline questionnaire, and post-study survey are
 * no longer embedded in the app. They are sent to participants directly via
 * email — see study_app/emails/ for the templates. `confirm:submission` is a
 * final in-app step that recaps all four task submissions before the
 * participant finishes the study.
 */

export const MASTER_STEP_IDS = [
  'onboarding:welcome',
  'onboarding:intro',
  'onboarding:guidelines',
  'check:comprehension',
  'task:1:first',
  'task:1:second',
  'task:2:first',
  'task:2:second',
  'confirm:submission',
];

export const MODALITY_LABEL = {
  nl: 'Natural-language description',
  gherkin: 'Gherkin / BDD description',
};

export function oppositeModality(modality) {
  return modality === 'gherkin' ? 'nl' : 'gherkin';
}
