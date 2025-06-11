
const merDirective = {
    name: 'mermaid-p',
    doc: 'An example directive for showing a nice random image at a custom size.',
    body: {
        type: String,
        required: true,
    },
    run(data) {
        const graph = btoa(unescape(encodeURIComponent( data.body)))
        const url = `https://mermaid.ink/img/${graph}?width=800&scale=2`;
        const img = { type: 'image', url };
        return [img];
    },
};

const plugin = { name: 'Custom Mermaid', directives: [merDirective] };

export default plugin;
