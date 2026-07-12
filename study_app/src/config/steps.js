/**
 * Static master configuration for every participant's flow.
 * Step IDs that contain `task:` are dynamically expanded into a concrete
 * task/modality step using the participant's assignment.
 */

export const MASTER_STEP_IDS = [
  'pre:consent',
  'pre:baseline',
  'onboarding:intro',
  'onboarding:guidelines',
  'check:comprehension',
  'task:1',
  'task:2',
  'post:feedback',
];

export const FORM_URLS = {
  // Replace with actual Google Form pre-fill URLs after the forms are created.
  // The `entry.<ID>=PID_PLACEHOLDER` part is required for the participant ID
  // to be pre-filled — FormStep.jsx substitutes PID_PLACEHOLDER with the
  // real pid at render time. Get the entry ID via Google Forms'
  // "Get pre-filled link" feature on the participant-ID field.
  // Example: https://docs.google.com/forms/d/e/FORM_ID/viewform?usp=pp_url&entry.123=PID_PLACEHOLDER
  'pre:consent': 'https://docs.google.com/forms/d/e/1FAIpQLSfjdS38AGDm8bDTCnHnIK84nEEtoLOEmkOTQ6hj_JEPJ_r_Cw/viewform?usp=pp_url&entry.1288115555=PID_PLACEHOLDER',
  'pre:baseline': 'https://docs.google.com/forms/d/e/1FAIpQLSfWdmJvb0X3cCGJ3nlDBp08JHEj54ANJRPsyxloN5sZs634fg/viewform?usp=pp_url&entry.1920052663=PID_PLACEHOLDER',
  'post:feedback': 'https://docs.google.com/forms/d/e/1FAIpQLScRaOclPLccPNmmZpzRiHzwxKWyisxoxvqkD6j6qwl5xp_Gvw/viewform?usp=pp_url&entry.1920052663=PID_PLACEHOLDER',
};

export const MODALITY_LABEL = {
  nl: 'Natural-language description',
  gherkin: 'Gherkin / BDD description',
};
