// import { DEFAULT_HANDLERS } from 'tex-to-myst';

const admonitionDirective = {
    name: 'nproof',
    doc: 'Callouts, or "admonitions", highlight a particular block of text that exists slightly apart from the narrative of your page, such as a note or a warning. \n\n The admonition kind can be determined by the directive name used (e.g. `:::{tip}` or `:::{note}`).',
    alias: [
        'requirement',
        'algorithm',
        'use-case',
        'test-card',
    ],
    arg: {
        type: 'myst',
        doc: 'The optional title of the admonition, if not supplied the admonition kind will be used.\n\nNote that the argument parsing is different from Sphinx, which does not allow named admonitions to have custom titles.',
    },
    options: {
        // ...commonDirectiveOptions('proof'),
        class: {
            type: String,
            doc: `CSS classes to add to your admonition. Special classes include:

- \`dropdown\`: turns the admonition into a \`<details>\` html element
- \`simple\`: an admonition with "simple" styles
- the name of an admonition, the first valid admonition name encountered will be used (e.g. \`tip\`). Note that if you provide conflicting class names, the first valid admonition name will be used.`,
        },
        icon: {
            type: Boolean,
            doc: 'Setting icon to false will hide the icon.',
        },
        open: {
            type: Boolean,
            doc: "Turn the admonition into a dropdown, if it isn't already, and set the open state.",
        },
    },
    body: {
        type: 'myst',
        doc: 'The body of the admonition. If there is no title and the body starts with bold text or a heading, that content will be used as the admonition title.',
    },
    run(data) {
        let toTitleCase = (str) => {
            return str.replace(
                /\w\S*/g,
                text => text.charAt(0).toUpperCase() + text.substring(1).toLowerCase()
            );
        };
        const children = [];
        if (data.arg) {
            children.push({
                type: 'admonitionTitle',
                children: [{ type: 'text', value: toTitleCase(`${data.name.replace('-', ' ')}: ${data.arg[0].value}`) }]
            });
        }
        if (data.body) {
            children.push(...data.body);
        }
        const admonition = {
            type: 'admonition',
            kind: 'admonition',
            children: children,
        };
        if (data.options?.icon === false) {
            admonition.icon = false;
        }
        if (typeof data.options?.open === 'boolean') {
            if (!admonition.class?.split(' ').includes('dropdown')) {
                admonition.class = `${admonition.class ?? ''} dropdown`.trim();
            }
            if (data.options.open) admonition.open = true;
        }


        // addCommonDirectiveOptions(data, admonition);
        return [admonition];
    },
};

// const latexDirective = {
//     name: 'myst:tex-list',
//     run() {
//         const keys = Object.keys(DEFAULT_HANDLERS);
//         const macros = keys
//             .filter((k) => k.startsWith('macro_'))
//             .map((k) => ({
//                 type: 'listItem',
//                 children: [{ type: 'inlineCode', value: `\\${k.replace('macro_', '')}` }],
//             }));
//         const environments = keys
//             .filter((k) => k.startsWith('env_'))
//             .map((k) => ({
//                 type: 'listItem',
//                 children: [{ type: 'inlineCode', value: `\\begin{${k.replace('env_', '')}}` }],
//             }));
//         return [
//             {
//                 type: 'details',
//                 children: [
//                     { type: 'summary', children: [{ type: 'text', value: 'LaTeX Macros' }] },
//                     { type: 'list', children: macros },
//                 ],
//             },
//             {
//                 type: 'details',
//                 children: [
//                     { type: 'summary', children: [{ type: 'text', value: 'LaTeX Environments' }] },
//                     { type: 'list', children: environments },
//                 ],
//             },
//         ];
//     },
// };


const plugin = { name: 'Custom requirement', directives: [admonitionDirective] };

export default plugin;
